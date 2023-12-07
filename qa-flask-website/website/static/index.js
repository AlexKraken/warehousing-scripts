function deleteBarcode(barcode) {
    fetch('/delete-barcode', {
        method: 'POST',
        body: JSON.stringify({ barcode: barcode }),
    }).then((_res) => {
        window.location.href = "/barcode";
    })
}
