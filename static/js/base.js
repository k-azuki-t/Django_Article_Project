addEventListener('DOMContentLoaded', function() {
    const path = window.location.pathname;
    let navbarButton = '';

    if (path.includes('articles')) {
        navbarButton = document.getElementById('articles');
    } else if  (path.includes('product')) {
        navbarButton = document.getElementById('product');
    }else if (path.includes('about/this_site')) {
        navbarButton = document.getElementById('about-this-site');
    } else if (path.includes('about/kurage')) {
        navbarButton = document.getElementById('about-kurage');
    } else if  (path.includes('accounts')) {
        navbarButton = document.getElementById('accounts');
    }

    navbarButton.classList.add('active');
    console.log(navbarButton);
})