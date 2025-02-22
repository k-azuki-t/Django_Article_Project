// お気に入り登録
async function registerFavorite() {

    const articleId = document.getElementById('article-id').textContent;
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    const response = await fetch(`favorite/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({
            article_id: articleId,
        }),
    });
    const responseData = await response.json();

    if (response.ok) {
        const favoriteButton =  document.querySelector('.favorite-icon-container i');
        const isFavorited = responseData['is_favorited'];

        if (isFavorited) {
            favoriteButton.classList.add('bi-suit-heart-fill');
            favoriteButton.classList.remove('bi-suit-heart');
        } else {
            favoriteButton.classList.add('bi-suit-heart');
            favoriteButton.classList.remove('bi-suit-heart-fill');
        }
    } else {
        window.location.href = responseData['redirect_url'];
    }
}


// 閲覧回数のカウント
document.addEventListener('DOMContentLoaded', async function() {
    const articleId = document.getElementById('article-id');
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    if (articleId) {
        const response = await fetch(`addViewedCount/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({
                article_id: articleId,
            }),
        });
        const responseData = await response.text();

        if (!response.ok) {
            window.location.href = responseData['redirect_url'];
        }
    }
});