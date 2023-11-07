import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MemberList() {
  const [members, setMembers] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  // Helper function to load members
  const loadMembers = async (token, source) => {
    try {
      const response = await axios.get('http://localhost:8000/api/members/', {
        headers: { 'Authorization': `Bearer ${token}` },
        cancelToken: source.token
      });
      setMembers(response.data);
    } catch (error) {
      if (axios.isCancel(error)) {
        console.log('Request canceled due to component unmounting', error.message);
      } else if (error.response) {
        setError(`Error: ${error.response.data.detail}`);
      } else if (error.request) {
        setError("Error: No response received from server.");
      } else {
        setError(`Error: ${error.message}`);
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    const token = localStorage.getItem('jwtToken');
    const source = axios.CancelToken.source();

    if (token) {
      loadMembers(token, source);
    } else {
      setError("JWT token not found in local storage.");
      setLoading(false);
    }

    // Cleanup function
    return () => {
      source.cancel("Component unmounted, request cancelled");
    };
  }, []);

  if (loading) {
    return <p>Loading members...</p>;
  }

  if (error) {
    return <p style={{ color: 'red' }}>{error}</p>;
  }

  return (
    <div>
      <h2>Members List</h2>
      <ul>
        {members.map(member => (
          <li key={member.id}>{member.full_name}</li>
        ))}
      </ul>
    </div>
  );
}

export default MemberList;





