import * as React from "react";
import "./App.css";
import { Branches } from "./components/branches/Branches";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Main } from "./components/Main";
import { NotFound } from "./components/NotFound";
import { Sales } from "./components/Sales";
import { AddBranch } from "./components/branches/AddBranch";
import { AddSupplier } from "./components/suppliers/AddSupplier";
import { Suppliers } from "./components/suppliers/Suppliers";
import { SupplierPage } from "./components/suppliers/SupplierPage";
import { FilteredBranchesList } from "./components/branches/FilteredBranchesList";
import { BranchPage } from "./components/branches/BranchPage";

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
        <Route path="/suppliers/add" element={<AddSupplier />} />
        <Route path="/supplier/:id" element={<SupplierPage />} />
        <Route path="/branch/:city/:name/:_id" element={<FilteredBranchesList />} />
        <Route path="/branch/:city/:name" element={<FilteredBranchesList />} />
        <Route path="/branch/:city" element={<FilteredBranchesList />} />
      </Routes>
    </Router>
  );
}

export default App;
