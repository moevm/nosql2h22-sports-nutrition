import * as React from "react";
import { useEffect, useState } from "react";
import { Pagination } from "../pagination/Pagination";
import { HOST } from "../../constants";
import { getSupplierPage, importSuppliers } from "../../api/supplier";
import { Box, Button } from "@mui/material";
import { ExportPage } from "../export/ExportPage";
import { exportSuppliersPage } from "../../api/export";
import { ImportPage } from "../import/ImportPage";
import "./Suppliers.scss";

const pageSize = 15;

export const SuppliersList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);
  const [lastPage, setLastPage] = useState(false);
  const [exportDialogOpen, setExportDialogOpen] = useState(false);
  const [importDialogOpen, setImportDialogOpen] = useState(false);

  useEffect(() => {
    getSupplierPage(pageSize, currentPage)
      .then((response) => response.json())
      .then((json) => {
        if (json.items.length) {
          setData(json.items);
          setLastPage(json.items.length < pageSize);
        }
      });
  }, [currentPage]);

  return (
    <Box>
      <Button onClick={() => setExportDialogOpen(!exportDialogOpen)}> Export </Button>
      <ExportPage isOpen={exportDialogOpen} setOpen={setExportDialogOpen}
                  requestFunc={exportSuppliersPage} />
      <Button onClick={() => setImportDialogOpen(!importDialogOpen)}> Import </Button>
      <ImportPage isOpen={importDialogOpen} setOpen={setImportDialogOpen}
                  requestFunc={importSuppliers}
                  setData={setData}
                  setLastPage={setLastPage}
                  lastPage={lastPage}
                  currentPage={currentPage}
                  dataList={data}
                  pageSize={pageSize}
                  getPageApi={getSupplierPage} />
      <table >
        <thead>
        <tr>
          <th>Supplier Id</th>
          <th>Name</th>
        </tr>
        </thead>
        <tbody>
        {data.map((item) => {
          return (
            <tr key={item._id} className="suppliers-table">
              <td className="cell-id">
                <a href={`${HOST}8080/supplier/${item._id}`}>
                  {item._id}
                </a></td>
              <td>{item.name}</td>
            </tr>
          );
        })}
        </tbody>
      </table>
      <Pagination
        lastPage={lastPage}
        className="pagination-bar"
        currentPage={currentPage}
        onPageChange={(page: number) => setCurrentPage(page)}
      />
    </Box>
  );
};
