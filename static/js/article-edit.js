const dropArea = document.querySelector('.drop-area');
const fileInput = document.getElementById('id_header_img_url');

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
        img.style.objectFit = 'cover';
        img.style.width = '100%';
        img.style.height = '100%';
        dropArea.appendChild(img);
        dropArea.querySelector('.img-form-message').style.display = 'none';
    }

    // 画像フォーム内の要素を非表示にする
    dropArea.querySelector('.bi-image').style.display = 'none';
    dropArea.querySelector('#id_header_img_url').style.display = 'none';
}

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

// 記事本文の記載する領域とプレビュー領域を出し分ける関数
function changeDisplayStatus(status) {

    if (window.location.pathname !== '/articles/edit/' ) {
        return;
    }

    if (status === 'edit') {
        document.querySelector('.markdownx-editor').style.display = '';
        document.querySelector('.markdownx-preview').style.display = 'None';
    } else if (status === 'preview') {
        document.querySelector('.markdownx-editor').style.display = 'None';
        document.querySelector('.markdownx-preview').style.display = '';
    }
}

// 初期状態は記事を記載する領域を出すように指定WW
document.addEventListener("DOMContentLoaded", changeDisplayStatus('edit'));