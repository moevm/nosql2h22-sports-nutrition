import * as React from "react";
import "./App.css";
import {Branches} from "./components/branches/Branches";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import {Main} from "./components/Main";
import {NotFound} from "./components/NotFound";
import {Sales} from "./components/sales/Sales";
import {AddSupplier} from "./components/suppliers/AddSupplier";
import {Suppliers} from "./components/suppliers/Suppliers";
import {SupplierPage} from "./components/suppliers/SupplierPage";
import {BranchPage} from "./components/branches/BranchPage";
import {EmployeePage} from "./components/employees/EmployeePage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/branches" element={<Branches />} />
        <Route path="/suppliers" element={<Suppliers />} />
        <Route path="/sales" element={<Sales />} />
        <Route path="*" element={<NotFound />} />
        <Route path="/suppliers/add" element={<AddSupplier />} />
        <Route path="/supplier/:id" element={<SupplierPage />} />
        <Route path="/employee/:id" element={<EmployeePage />} />
        <Route path="/branch/id/:_id" element={<BranchPage />} />
      </Routes>
    </Router>
  );
}

export default App;
