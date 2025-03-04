const dropArea = document.querySelector('.drop-area');
const fileInput = document.getElementById('id_header_img_url');
const elements = document.getElementsByClassName('markdownx');
const path = window.location.pathname;

// dropArea関連の関数（ここから）
// 添付した画像ファイルを表示する関数
function handleFile(imgFIle) {
    const reader = new FileReader();

    reader.readAsDataURL(imgFIle);
    reader.onload = (e) => {
        // 画像がすでに表示されている場合は削除
        if (dropArea.querySelector('img')) {
            dropArea.querySelector('img').remove();
        }
        // フォームに選択した画像を表示
        const img = document.createElement('img');
        img.src = e.target.result;
        img.alt = 'Uploaded Image';
        img.setAttribute('class', 'article-header-img');
        dropArea.appendChild(img);
        dropArea.querySelector('.img-form-message').style.display = 'none';
    }

    // 画像フォーム内の要素を非表示にする
    dropArea.querySelector('.bi-image').style.display = 'none';
    dropArea.querySelector('#id_header_img_url').style.display = 'none';
}


// 記事編集画面でのみaddEventListenerを実行
if (path.includes('/articles/edit/')) {

    // エクスプローラーでのファイル選択時の処理
    fileInput.addEventListener('change', (e) => {
        // 記事編集画面でのみ処理を実行
        if (window.location.pathname == '/articles/edit/') {
            const imgFile = e.target.files[0];
            if (imgFile && imgFile.type.startsWith('image/')) {
                handleFile(imgFile);
            } else {
                fileInput.value = '';
                alert('画像ファイルを選択してください');
            }
        }
    });

    // ドラッグ&ドロップ時の処理
    dropArea.addEventListener('drop', (e) => {
        if (window.location.pathname == '/articles/edit/') {

            // input要素にファイルをセットするためのDataTransferオブジェクトを作成
            const imgFile = e.dataTransfer.files[0];
            const dataTransfer = new DataTransfer();

            // 選択したファイルが画像ファイルかどうかを判定
            if (imgFile && imgFile.type.startsWith('image/')) {
                // input要素にファイルをセット
                dataTransfer.items.add(imgFile);
                fileInput.files = dataTransfer.files;
                handleFile(imgFile);
            } else {
                alert('画像ファイルを選択してください');
            }
        }
    });

    // ドロップエリアのクリック時の処理
    dropArea.addEventListener('click', () => {
        if (window.location.pathname == '/articles/edit/') {
            fileInput.click();
        }
    });
}


// 記事本文の記載するフィールドとプレビューフィールドを出し分ける関数
function changeDisplayStatus(status) {

    // 記事編集画面でのみ実行されるよう指定
    if (window.location.pathname !== '/articles/edit/' ) {
        return;
    }

    if (status === 'edit') {
        // 編集フィールドを表示
        document.querySelector('.markdownx-editor').style.display = '';
        document.querySelector('.markdownx-preview').style.display = 'None';
        // ボタンの色を変更
        document.getElementById('edit').style.backgroundColor = '#575757';
        document.getElementById('edit').style.color = 'white';
        document.getElementById('preview').style.backgroundColor = 'white';
        document.getElementById('preview').style.color = 'black';

    } else if (status === 'preview') {
        // プレビューを表示
        document.querySelector('.markdownx-editor').style.display = 'None';
        document.querySelector('.markdownx-preview').style.display = '';
        // ボタンの色を変更
        document.getElementById('edit').style.backgroundColor = 'white';
        document.getElementById('edit').style.color = 'black';
        document.getElementById('preview').style.backgroundColor = '#575757';
        document.getElementById('preview').style.color = 'white';
    }
}

// 初期状態は記事を記載する領域を出すように指定
document.addEventListener("DOMContentLoaded", changeDisplayStatus('edit'));
// dropArea関連の関数（ここまで）


// コードブロックに色を付ける処理（highlight.js）
for (let element of elements) {
    element.addEventListener('markdownx.update', event => {
        for (let block of document.querySelectorAll('pre code')) {
            hljs.highlightElement(block);
        }
    });
}