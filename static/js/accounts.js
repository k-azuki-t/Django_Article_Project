// パスワードの条件を表示する関数
function displayPassExplanation() {
    const container = document.querySelector('.message-container');
    container.innerHTML = `
        <div class="item-container message">
            パスワードは以下を満たす必要があります。<br>
            ・メールアドレスと類似しない<br>
            ・8文字以上である<br>
            ・簡易的でない/全て数字ではない
            <div class="circle-container">
            <svg viewBox="0 0 50 50" width="50px" height="50px">
                <circle
                cx="25"
                cy="25"
                r="15"
                fill="transparent"
                stroke="#fff"
                stroke-width="6"
                class="time-circle"
                ></circle>
            </svg>
            </div>
        </div>
        `;
    const message = container.querySelector('.message');
    
    setTimeout(() => {
        message.style.display = 'none';
    }, 4000);

}