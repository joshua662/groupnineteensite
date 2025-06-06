function showToast(message) {
    const toast = document.getElementById('toast-message');
    const toastText = document.getElementById('toast-text');
    toastText.textContent = message;
    toast.classList.remove('hidden');
    setTimeout(() => {
        toast.classList.add('hidden');
    }, 3000);
} 