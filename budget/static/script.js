// Function to show the corresponding page when the sidebar link is clicked
function showPage(page) {
    // Get all page content elements
    const pages = document.querySelectorAll('.page-content');
    
    // Temporarily hide all pages with a fade-out effect
    pages.forEach(p => {
        p.classList.add('hidden');  // Fade out all pages
        p.classList.remove('active');
    });

    // Delay adding the 'active' class to the selected page to allow fade-out transition
    setTimeout(() => {
        const selectedPage = document.getElementById(page);
        selectedPage.classList.remove('hidden');
        selectedPage.classList.add('active');  // Fade in the selected page
    }, 300);  // Match the transition time in CSS (0.3s)
}



// Set default page (Home) to be displayed when the page loads
document.addEventListener('DOMContentLoaded', () => {
    showPage('home');


});