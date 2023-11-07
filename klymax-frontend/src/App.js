import React from 'react';
// Removed the unused Login import
import MenuBar from './components/Menubar';
// Removed the incorrect import for memberList
import MemberList from './pages/Members/memberList'; // Make sure this path is correct

const App = () => {
  return (
    <>
      <MenuBar menuItems={["Members", "Events", "Contents"]} />
      <MemberList />
    </>
  );
};

export default App;







