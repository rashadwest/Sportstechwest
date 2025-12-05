/**
 * Stripe Payment Integration for BallCODE Books
 * Ready to use - just add your Stripe API keys
 */

class StripePaymentIntegration {
    constructor() {
        // Replace with your actual Stripe keys
        this.stripePublicKey = 'pk_test_YOUR_STRIPE_PUBLIC_KEY';
        this.stripeSecretKey = 'sk_test_YOUR_STRIPE_SECRET_KEY'; // Server-side only
        this.stripe = null;
        this.init();
    }
    
    /**
     * Initialize Stripe
     */
    init() {
        if (!window.Stripe) {
            const script = document.createElement('script');
            script.src = 'https://js.stripe.com/v3/';
            script.onload = () => {
                this.stripe = Stripe(this.stripePublicKey);
                this.setupPaymentForm();
            };
            document.head.appendChild(script);
        } else {
            this.stripe = Stripe(this.stripePublicKey);
            this.setupPaymentForm();
        }
    }
    
    /**
     * Setup payment form
     */
    setupPaymentForm() {
        // Create Stripe Elements
        const elements = this.stripe.elements();
        
        // Create card element
        const cardElement = elements.create('card', {
            style: {
                base: {
                    fontSize: '16px',
                    color: '#424770',
                    '::placeholder': {
                        color: '#aab7c4',
                    },
                },
                invalid: {
                    color: '#9e2146',
                },
            },
        });
        
        // Mount card element
        const cardContainer = document.getElementById('card-element');
        if (cardContainer) {
            cardElement.mount(cardContainer);
        }
        
        this.cardElement = cardElement;
    }
    
    /**
     * Process single book payment
     */
    async processSingleBookPayment(bookId, bookData) {
        try {
            // Create payment intent on server
            const response = await fetch('/api/stripe/create-payment-intent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    amount: Math.round(bookData.price * 100), // Convert to cents
                    currency: 'usd',
                    metadata: {
                        bookId: bookId,
                        bookName: bookData.name,
                        type: 'single'
                    }
                })
            });
            
            const { clientSecret } = await response.json();
            
            // Confirm payment
            const result = await this.stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: this.cardElement,
                    billing_details: {
                        name: document.getElementById('cardholder-name')?.value || 'Customer'
                    }
                }
            });
            
            if (result.error) {
                throw new Error(result.error.message);
            }
            
            return {
                success: true,
                paymentIntent: result.paymentIntent
            };
            
        } catch (error) {
            console.error('Stripe payment error:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }
    
    /**
     * Process bundle payment
     */
    async processBundlePayment(bundleData) {
        try {
            // Create payment intent on server
            const response = await fetch('/api/stripe/create-payment-intent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    amount: Math.round(bundleData.price * 100), // Convert to cents
                    currency: 'usd',
                    metadata: {
                        type: 'bundle',
                        books: bundleData.books.join(',')
                    }
                })
            });
            
            const { clientSecret } = await response.json();
            
            // Confirm payment
            const result = await this.stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: this.cardElement,
                    billing_details: {
                        name: document.getElementById('cardholder-name')?.value || 'Customer'
                    }
                }
            });
            
            if (result.error) {
                throw new Error(result.error.message);
            }
            
            return {
                success: true,
                paymentIntent: result.paymentIntent
            };
            
        } catch (error) {
            console.error('Stripe payment error:', error);
            return {
                success: false,
                error: error.message
            };
        }
    }
    
    /**
     * Server-side payment intent creation (Node.js example)
     */
    async createPaymentIntentServerSide(amount, currency, metadata) {
        // This would be on your server (Node.js example)
        /*
        const stripe = require('stripe')(this.stripeSecretKey);
        
        const paymentIntent = await stripe.paymentIntents.create({
            amount: amount,
            currency: currency,
            metadata: metadata
        });
        
        return paymentIntent.client_secret;
        */
    }
}

// Initialize Stripe integration
const stripeIntegration = new StripePaymentIntegration();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = StripePaymentIntegration;
}



