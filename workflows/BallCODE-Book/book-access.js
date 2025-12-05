/**
 * BallCODE Book Access Control System
 * Manages password protection for digital books
 */

// Book passwords configuration
// Change these passwords as needed
const BOOK_PASSWORDS = {
    'watsonx1': 'watsonx1',  // Change this password
    'watsonx2': 'watsonx2',  // Change this password
    'ciscoiq': 'ciscoiq'     // Change this password (if keeping)
};

// Get book ID from URL or page
function getBookId() {
    const path = window.location.pathname;
    const filename = window.location.pathname.split('/').pop() || '';
    
    // Check for WatsonX books
    if (path.includes('watsonx1') || filename.includes('watsonx1')) return 'watsonx1';
    if (path.includes('watsonx2') || filename.includes('watsonx2')) return 'watsonx2';
    // Legacy support
    if (path.includes('watson1') || filename.includes('watson1')) return 'watsonx1';
    if (path.includes('watson2') || filename.includes('watson2')) return 'watsonx2';
    if (path.includes('ciscoiq') || filename.includes('ciscoiq')) return 'ciscoiq';
    return null;
}

// Check if user has access to a book
function hasAccess(bookId) {
    const accessKey = `ballcode_book_access_${bookId}`;
    const accessTime = sessionStorage.getItem(accessKey);
    if (!accessTime) return false;
    
    // Access expires after 4 hours
    const now = Date.now();
    const accessExpiry = parseInt(accessTime) + (4 * 60 * 60 * 1000);
    return now < accessExpiry;
}

// Grant access to a book
function grantAccess(bookId) {
    const accessKey = `ballcode_book_access_${bookId}`;
    sessionStorage.setItem(accessKey, Date.now().toString());
}

// Revoke access (for logout/clear)
function revokeAccess(bookId) {
    const accessKey = `ballcode_book_access_${bookId}`;
    sessionStorage.removeItem(accessKey);
}

// Verify password for a book
function verifyPassword(bookId, password) {
    const correctPassword = BOOK_PASSWORDS[bookId];
    if (!correctPassword) return false;
    return password === correctPassword;
}

// Show password entry modal
function showPasswordModal(bookId, bookName) {
    const modal = document.createElement('div');
    modal.id = 'password-modal';
    modal.innerHTML = `
        <div class="password-modal-overlay">
            <div class="password-modal-content">
                <h2>🔒 Password Required</h2>
                <p>This book is password protected. Please enter the password to continue.</p>
                <p class="book-name"><strong>${bookName}</strong></p>
                <form id="password-form">
                    <input 
                        type="password" 
                        id="password-input" 
                        placeholder="Enter password" 
                        required 
                        autofocus
                    >
                    <div id="password-error" class="error-message"></div>
                    <div class="password-buttons">
                        <button type="submit" class="btn-primary">Access Book</button>
                        <button type="button" class="btn-secondary" onclick="window.location.href='/'">Cancel</button>
                    </div>
                </form>
                <p class="password-help">Need access? Contact your teacher for the password.</p>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    const form = document.getElementById('password-form');
    const input = document.getElementById('password-input');
    const errorDiv = document.getElementById('password-error');
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const password = input.value.trim();
        
        if (!password) {
            showError('Please enter a password');
            return;
        }
        
        if (verifyPassword(bookId, password)) {
            grantAccess(bookId);
            modal.remove();
            // Reload page to show content
            window.location.reload();
        } else {
            showError('Incorrect password. Please try again.');
            input.value = '';
            input.focus();
        }
    });
    
    function showError(message) {
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
        setTimeout(() => {
            errorDiv.style.display = 'none';
        }, 5000);
    }
}

// Initialize access control on page load
function initBookAccess() {
    const bookId = getBookId();
    if (!bookId) return;
    
    if (!hasAccess(bookId)) {
        // Get book name from page title or use book ID
        const bookName = document.title.replace('BallCODE: ', '').replace(' - Digital Book', '') || bookId;
        showPasswordModal(bookId, bookName);
    } else {
        // User has access, show content
        const protectedContent = document.getElementById('protected-content');
        if (protectedContent) {
            protectedContent.style.display = 'block';
        }
    }
}

// Add CSS for password modal
function addPasswordModalStyles() {
    const style = document.createElement('style');
    style.textContent = `
        #password-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .password-modal-overlay {
            background: rgba(0, 0, 0, 0.7);
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .password-modal-content {
            background: white;
            border-radius: 12px;
            padding: 40px;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            text-align: center;
        }
        
        .password-modal-content h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 2em;
        }
        
        .password-modal-content p {
            color: #666;
            margin-bottom: 20px;
            line-height: 1.6;
        }
        
        .book-name {
            font-size: 1.2em;
            color: #667eea;
            margin-bottom: 30px;
        }
        
        #password-form {
            margin: 30px 0;
        }
        
        #password-input {
            width: 100%;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 1.1em;
            margin-bottom: 15px;
            transition: border-color 0.3s;
        }
        
        #password-input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .error-message {
            color: #dc3545;
            margin-bottom: 15px;
            display: none;
            font-size: 0.9em;
        }
        
        .password-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            margin-top: 20px;
        }
        
        .btn-primary, .btn-secondary {
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-primary {
            background: #667eea;
            color: white;
        }
        
        .btn-primary:hover {
            background: #764ba2;
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
        
        .btn-secondary:hover {
            background: #5a6268;
        }
        
        .password-help {
            margin-top: 20px;
            font-size: 0.9em;
            color: #999;
        }
        
        #protected-content {
            display: none;
        }
    `;
    document.head.appendChild(style);
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        addPasswordModalStyles();
        initBookAccess();
    });
} else {
    addPasswordModalStyles();
    initBookAccess();
}

