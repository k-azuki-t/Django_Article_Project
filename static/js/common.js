// メッセージをDOM上から消す処理
addEventListener('DOMContentLoaded', () => {

    const message = document.querySelector('.message');
    console.log(message)

    if (message) {
        setTimeout(() => {
            message.style.display = 'none';
          }, 4000);
    }
})