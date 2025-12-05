/**
 * BallCODE Book Paywall System
 * Handles payment processing, purchase verification, and access control
 */

class BookPaywallSystem {
    constructor() {
        this.stripePublicKey = 'pk_test_YOUR_STRIPE_PUBLIC_KEY'; // Replace with actual key
        this.paypalClientId = 'YOUR_PAYPAL_CLIENT_ID'; // Replace with actual ID
        this.apiEndpoint = '/api/payments'; // Your payment API endpoint
    }
    
    /**
     * Initialize payment system
     */
    init() {
        this.loadStripe();
        this.loadPayPal();
        this.checkPurchaseStatus();
    }
    
    /**
     * Load Stripe.js
     */
    loadStripe() {
        if (!window.Stripe) {
            const script = document.createElement('script');
            script.src = 'https://js.stripe.com/v3/';
            script.onload = () => {
                this.stripe = Stripe(this.stripePublicKey);
            };
            document.head.appendChild(script);
        }
    }
    
    /**
     * Load PayPal SDK
     */
    loadPayPal() {
        if (!window.paypal) {
            const script = document.createElement('script');
            script.src = 'https://www.paypal.com/sdk/js?client-id=' + this.paypalClientId + '&currency=USD';
            script.onload = () => {
                this.paypalLoaded = true;
            };
            document.head.appendChild(script);
        }
    }
    
    /**
     * Check if book is purchased
     */
    checkPurchaseStatus(bookId) {
        // Check localStorage first (client-side)
        const purchased = localStorage.getItem(`book-${bookId}-purchased`);
        const bundlePurchased = localStorage.getItem('bundle-purchased');
        
        if (purchased === 'true' || bundlePurchased === 'true') {
            return true;
        }
        
        // Check server-side (if user is logged in)
        return this.checkServerPurchaseStatus(bookId);
    }
    
    /**
     * Check purchase status on server
     */
    async checkServerPurchaseStatus(bookId) {
        try {
            const response = await fetch(`${this.apiEndpoint}/check-purchase?bookId=${bookId}`);
            const data = await response.json();
            return data.purchased || false;
        } catch (error) {
            console.error('Error checking purchase status:', error);
            return false;
        }
    }
    
    /**
     * Process single book purchase
     */
    async purchaseSingleBook(bookId, paymentMethod = 'stripe') {
        const bookData = {
            id: bookId,
            name: `BallCODE Book ${bookId} - Dribble Level ${bookId}`,
            price: 9.99,
            type: 'single'
        };
        
        if (paymentMethod === 'stripe') {
            return await this.processStripePayment(bookData);
        } else if (paymentMethod === 'paypal') {
            return await this.processPayPalPayment(bookData);
        }
    }
    
    /**
     * Process bundle purchase
     */
    async purchaseBundle(paymentMethod = 'stripe') {
        const bundleData = {
            name: 'BallCODE Complete Bundle - All 7 Books',
            price: 49.99,
            type: 'bundle',
            books: [1, 2, 3, 4, 5, 6, 7]
        };
        
        if (paymentMethod === 'stripe') {
            return await this.processStripePayment(bundleData);
        } else if (paymentMethod === 'paypal') {
            return await this.processPayPalPayment(bundleData);
        }
    }
    
    /**
     * Process payment via Stripe
     */
    async processStripePayment(productData) {
        try {
            // Create payment intent on server
            const response = await fetch(`${this.apiEndpoint}/create-intent`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(productData)
            });
            
            const { clientSecret } = await response.json();
            
            // Confirm payment with Stripe
            const result = await this.stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: cardElement, // Stripe card element
                    billing_details: {
                        name: 'Customer Name' // Get from form
                    }
                }
            });
            
            if (result.error) {
                throw new Error(result.error.message);
            }
            
            // Payment successful
            await this.handlePurchaseSuccess(productData);
            return { success: true, result };
            
        } catch (error) {
            console.error('Stripe payment error:', error);
            return { success: false, error: error.message };
        }
    }
    
    /**
     * Process payment via PayPal
     */
    async processPayPalPayment(productData) {
        return new Promise((resolve, reject) => {
            paypal.Buttons({
                createOrder: (data, actions) => {
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: productData.price.toString()
                            },
                            description: productData.name
                        }]
                    });
                },
                onApprove: async (data, actions) => {
                    const order = await actions.order.capture();
                    
                    // Payment successful
                    await this.handlePurchaseSuccess(productData);
                    resolve({ success: true, order });
                },
                onError: (err) => {
                    reject({ success: false, error: err });
                }
            }).render('#paypal-button-container');
        });
    }
    
    /**
     * Handle successful purchase
     */
    async handlePurchaseSuccess(productData) {
        // Save purchase status locally
        if (productData.type === 'single') {
            localStorage.setItem(`book-${productData.id}-purchased`, 'true');
        } else if (productData.type === 'bundle') {
            localStorage.setItem('bundle-purchased', 'true');
            // Mark all books as purchased
            productData.books.forEach(bookId => {
                localStorage.setItem(`book-${bookId}-purchased`, 'true');
            });
        }
        
        // Save purchase on server (if user is logged in)
        await this.savePurchaseOnServer(productData);
        
        // Unlock content
        this.unlockContent(productData);
        
        // Show success message
        this.showSuccessMessage(productData);
    }
    
    /**
     * Save purchase on server
     */
    async savePurchaseOnServer(productData) {
        try {
            await fetch(`${this.apiEndpoint}/save-purchase`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    productData,
                    timestamp: new Date().toISOString(),
                    userId: this.getUserId() // If user is logged in
                })
            });
        } catch (error) {
            console.error('Error saving purchase:', error);
        }
    }
    
    /**
     * Unlock content after purchase
     */
    unlockContent(productData) {
        // Hide paywall
        const paywallElement = document.getElementById('paywall');
        if (paywallElement) {
            paywallElement.style.display = 'none';
        }
        
        // Enable video playback
        const videoElement = document.getElementById('book-video');
        if (videoElement) {
            videoElement.removeAttribute('controls');
            videoElement.play();
        }
        
        // Show unlocked message
        this.showUnlockedMessage();
    }
    
    /**
     * Show success message
     */
    showSuccessMessage(productData) {
        const message = productData.type === 'single' 
            ? `Book ${productData.id} unlocked! Enjoy your story!`
            : 'All 7 books unlocked! Enjoy your complete BallCODE collection!';
        
        alert(message);
    }
    
    /**
     * Show unlocked message
     */
    showUnlockedMessage() {
        // Can be customized with a nice UI component
        console.log('Content unlocked!');
    }
    
    /**
     * Get user ID (if logged in)
     */
    getUserId() {
        // Implement based on your authentication system
        return localStorage.getItem('userId') || null;
    }
}

// Initialize paywall system
const paywallSystem = new BookPaywallSystem();
paywallSystem.init();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BookPaywallSystem;
}



