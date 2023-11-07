import React, { useEffect, useState } from 'react';
import { DataGrid } from '@mui/x-data-grid';

// Define your columns based on the Member model's fields
const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'joinDate', headerName: 'Join Date', width: 100 },
  { field: 'membershipStatus', headerName: 'Status', width: 120 },
  { field: 'memberId', headerName: 'Member ID', width: 130 },
  { field: 'fullName', headerName: 'Full Name', width: 150 },
  { field: 'nickName', headerName: 'Nickname', width: 130 },
  { field: 'emailAddress', headerName: 'Email', width: 200 },
  { field: 'phoneNumber', headerName: 'Phone Number', width: 130 },
  { field: 'yearJoiningKlymax', headerName: 'Year Joined Klymax', width: 160 },
  { field: 'yearJoiningFoundation', headerName: 'Year Joined Foundation', width: 180 },
  { field: 'continent', headerName: 'Continent', width: 120 },
  { field: 'country', headerName: 'Country', width: 120 },

];

export default function MemberList() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    // Updated fetch URL to include 'api/' prefix
    fetch('http://localhost:8000/api/members/')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        // Assuming the backend sends data in the format that matches the column definitions
        setMembers(data);
      })
      .catch((error) => {
        console.error('Failed to fetch members:', error);
      });
  }, []);

  return (
    <div style={{ height: 700, width: '100%' }}>
      <DataGrid
        rows={members}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 5 },
          },
        }}
        pageSizeOptions={[5, 10, 15]}
        checkboxSelection
      />
    </div>
  );
}
