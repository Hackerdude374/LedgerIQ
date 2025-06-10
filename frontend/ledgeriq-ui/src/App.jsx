import React from 'react';
import UploadForm from './components/UploadForm';
import ReportLinks from './components/ReportLinks';
import LoginForm from './components/LoginForm';

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>LedgerIQ - Upload Transactions</h1>
      <UploadForm />
      <ReportLinks />
    </div>
  );
}

export default App;
