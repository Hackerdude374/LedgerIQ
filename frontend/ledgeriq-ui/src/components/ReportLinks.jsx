import React from 'react';

function ReportLinks() {
  return (
    <div>
      <h2>Download Reports</h2>
      <ul>
        <li><a href="http://localhost:5000/get/monthly_report.pdf" download>Download PDF</a></li>
        <li><a href="http://localhost:5000/get/monthly_report.xlsx" download>Download Excel</a></li>
        <li><a href="http://localhost:5000/get/charts/bar_chart.png" target="_blank">View Bar Chart</a></li>
        <li><a href="http://localhost:5000/get/charts/pie_chart.png" target="_blank">View Pie Chart</a></li>
      </ul>
    </div>
  );
}

export default ReportLinks;
