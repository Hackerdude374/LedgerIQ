import React, { useState } from 'react';

function UploadForm() {
  const [file, setFile] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    await fetch('http://localhost:5000/process', {
      method: 'POST',
      body: formData
    });

    alert('Processing complete! Download reports from below.');
  };

  const handleStripeFetch = async () => {
    await fetch('http://localhost:5000/stripe');
    alert('Stripe data processed! Download reports below.');
  };

  return (
    <div>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} required />
        <button type="submit">Upload & Process</button>
      </form>
      <br />
      <button onClick={handleStripeFetch}>Fetch Stripe Transactions</button>
    </div>
  );
}

export default UploadForm;
