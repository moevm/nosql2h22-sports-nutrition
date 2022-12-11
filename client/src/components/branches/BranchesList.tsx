import * as React from "react";
import {useEffect, useState} from "react";
import "./Branches.scss";
import {Pagination} from "../pagination/Pagination";
import {getBranchesPage, importBranches} from "../../api/branch";
import {Box, Button} from "@mui/material";
import {ExportPage} from "../export/ExportPage";
import {exportBranchesPage} from "../../api/export";
import {ImportPage} from "components/import/ImportPage";
import {BranchesTable} from "./BranchesTable";

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

       <BranchesTable branches={data} forPagination={true} />
      <Pagination
        lastPage={lastPage}
        className="pagination-bar"
        currentPage={currentPage}
        onPageChange={(page: number) => setCurrentPage(page)}
      />
    </Box>
  );
};
