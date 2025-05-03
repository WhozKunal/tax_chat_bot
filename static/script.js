document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const inputPopup = document.getElementById('inputPopup');
    const inputVideo = document.getElementById('inputVideo');
    const processButton = document.getElementById('processButton');
    const detectedPopup = document.getElementById('detectedPopup');
    const downloadHeading = document.getElementById('downloadHeading');
    const downloadLink = document.getElementById('downloadLink');

    // Drag and drop functionality
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const file = e.dataTransfer.files[0];
        handleFile(file);
    });

    // Click to browse
    fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        if (file) handleFile(file);
    });

    // Handle file selection
    function handleFile(file) {
        const maxSizeMB = 100;
        if (file.size > maxSizeMB * 1024 * 1024) {
            alert('File size exceeds 100MB!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error('Upload failed: ' + response.statusText);
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error('Upload error:', data.error);
                alert('Upload error: ' + data.error);
                return;
            }
            const fileURL = URL.createObjectURL(file);
            inputVideo.src = fileURL;
            inputVideo.play().catch(err => console.error('Input video play error:', err));
            inputPopup.style.display = 'block';
            processButton.dataset.filepath = data.filepath;
            detectedPopup.style.display = 'none';
            downloadHeading.style.display = 'none';
            downloadLink.style.display = 'none';
        })
        .catch(error => {
            console.error('Upload fetch error:', error);
            alert('Upload failed: ' + error.message);
        });
    }

    // Process button click
    processButton.addEventListener('click', () => {
        const filepath = processButton.dataset.filepath;
        if (!filepath) {
            alert('No file to process');
            return;
        }

        processButton.textContent = 'Processing...';
        processButton.disabled = true;

        fetch('/start_detection', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ filepath: filepath })
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(`Detection failed: ${err.error || response.statusText}`);
                });
            }
            return response.json();
        })
        .then(data => {
            processButton.textContent = 'Process';
            processButton.disabled = false;

            if (data.error) {
                console.error('Detection response error:', data.error);
                alert('Error: ' + data.error);
                return;
            }

            console.log('Download URL:', data.download_url);

            // Show heading and download button
            detectedPopup.style.display = 'block';
            downloadHeading.style.display = 'block';
            downloadLink.href = data.download_url;
            downloadLink.style.display = 'inline-block';
        })
        .catch(error => {
            console.error('Detection fetch error:', error);
            processButton.textContent = 'Process';
            processButton.disabled = false;
            alert('Detection failed: ' + error.message);
        });
    });

    // Close input popup only
    window.closeInputPopup = function() {
        inputPopup.style.display = 'none';
        inputVideo.src = '';
        URL.revokeObjectURL(inputVideo.src);
    };
});