// ページに応じてnavbarのボタンをアクティブにする処理
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
})

// ナビバーの表示非表示を切り替える処理
const navbar = document.querySelector('.navbar');
const mainContent = document.querySelector('.main-content');

function displayNavbar() {
    
    if (navbar.style.display === '') {
        mainContent.classList.add('slideOutRight');
        setTimeout(() => {
            mainContent.style.display = 'none';
            navbar.classList.add('slideinLeft');
            navbar.style.display = 'flex';
        }, 250);
    } else if (navbar.style.display === 'none') {
        mainContent.classList.replace('slideinRight', 'slideOutRight');
        setTimeout(() => {
            mainContent.style.display = 'none';
            navbar.classList.replace('slideOutLeft', 'slideinLeft');
            navbar.style.display = 'flex';
        }, 250);
    } else {
        navbar.classList.replace('slideinLeft', 'slideOutLeft');
        setTimeout(() => {
            navbar.style.display = 'none';
            mainContent.style.display = 'flex';
            mainContent.classList.replace('slideOutRight', 'slideinRight');
        }, 250);
    }
}


// メディアクエリによってナビバーの表示非表示を切り替える処理
const mediaQuery = window.matchMedia("(max-width: 900px)");
function handleMediaChange(e) {
    if (e.matches) {
    } else {
    // それ以外のとき（元に戻すなど）
    mainContent.classList.remove('slideOutRight');
    mainContent.classList.remove('slideinRight');
    navbar.classList.remove('slideinLeft');
    navbar.classList.remove('slideOutLeft');
    mainContent.style.display = null;
    navbar.style.display = null;
    mainContent.style.transform = "translateX(0)";
    navbar.style.transform = "translateX(0)";
    }
}
mediaQuery.addEventListener('change', handleMediaChange);