import * as React from "react";
import { useEffect, useState } from "react";
import "./Branches.scss";
import { Pagination } from "../pagination/Pagination";
import { HOST } from "../../constants";
import { getBranchesPage, importBranches } from "../../api/branch";
import { Box, Button } from "@mui/material";
import { ExportPage } from "../export/ExportPage";
import { exportBranchesPage } from "../../api/export";
import { ImportPage } from "components/import/ImportPage";

const pageSize = 15;

export const BranchesList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);
  const [lastPage, setLastPage] = useState(false);
  const [exportDialogOpen, setExportDialogOpen] = useState(false);
  const [importDialogOpen, setImportDialogOpen] = useState(false);

  useEffect(() => {
    getBranchesPage(pageSize, currentPage)
      .then((response) => response.json())
      .then((json) => {
        if (json.items.length) {
          setData(json.items);
          setLastPage(json.items.length < pageSize);
        }
      });
  }, [currentPage, getBranchesPage]);

  return (
    <Box>
      <Button onClick={() => setExportDialogOpen(!exportDialogOpen)}> Export </Button>
      <Button onClick={() => setImportDialogOpen(!importDialogOpen)}> Import </Button>
      <ExportPage isOpen={exportDialogOpen} setOpen={setExportDialogOpen}
                  requestFunc={exportBranchesPage} />
      <ImportPage isOpen={importDialogOpen} setOpen={setImportDialogOpen}
                  requestFunc={importBranches}
                  setData={setData} setLastPage={setLastPage}
                  lastPage={lastPage}
                  currentPage={currentPage}
                  dataList={data}
                  pageSize={pageSize}
                  getPageApi={getBranchesPage} />
      <table>
        <thead>
        <tr>
          <th>Branch Id</th>
          <th>Name</th>
          <th>Employees</th>
          <th>Stocks</th>
          <th>Location</th>
        </tr>
        </thead>
        <tbody>
        {data.map((item) => {
          return (
            <tr key={item._id} className="branches-table">
              <td className="cell-id"
              ><a href={`${HOST}8080/branch/id/${item._id}`}>
                {item._id}
              </a></td>
              <td>{item.name}</td>
              <td>{item.employees}</td>
              <td>{item.stocks}</td>
              <td>{item.city}</td>
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
