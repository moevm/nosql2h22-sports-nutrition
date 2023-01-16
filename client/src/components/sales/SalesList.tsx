import * as React from "react";
import {useEffect, useState} from "react";
import {Pagination} from "../pagination/Pagination";
import {getAllSales} from "../../api/sale";
import {Box, Button} from "@mui/material";
import {SalesTable} from "./SalesTable";

const pageSize = 15;

export const SalesList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);

  useEffect(() => {
    getAllSales()
      .then((response) => response.json())
      .then((json) => {
        if (json.items.length) {
          setData(json.items);
        }
      });
  }, [currentPage, getAllSales]);

  return (
    <Box>
       {/* <SalesTable sales={data} forPagination={true} /> */}
    </Box>
  );
};
