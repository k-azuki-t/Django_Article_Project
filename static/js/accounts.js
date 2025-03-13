// パスワードの条件を表示する関数
function displayPassExplanation() {
    const container = document.querySelector('.message-container');
    const message = document.createElement('div')
    message.setAttribute('class', 'item-container message');
    message.innerHTML = 'パスワードは以下を満たす必要があります。<br>・メールアドレスと類似しない<br>・8文字以上である<br>・簡易的でない/全て数字ではない';

    container.replaceChildren(message);
    setTimeout(() => {
        message.style.display = 'none';
    }, 4000);
}