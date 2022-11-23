import * as React from 'react';
import './App.css';
import { Branches } from './components/branches/Branches';
import { Suppliers } from './components/Suppliers';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Main } from './components/Main';
import { NotFound } from "./components/NotFound";
import { Sales } from "./components/Sales";
import { AddBranch } from "./components/branches/AddBranch";

function App() {
  return (
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/branches" element={<Branches />} />
          <Route path="/suppliers" element={<Suppliers />} />
          <Route path="/sales" element={<Sales />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/branches/add" element={<AddBranch />} />
        </Routes>
      </Router>
  );
}

export default App;