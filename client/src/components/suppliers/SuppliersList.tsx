import * as React from "react";
import { useEffect, useState } from "react";
import { Pagination } from "../pagination/Pagination";
import { HOST } from "../../constants";
import { getSupplierPage } from "../../api/supplier";

const pageSize = 15;

export const SuppliersList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);
  const [lastPage, setLastPage] = useState(false);

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
    <>
      <table>
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
    </>
  );
};
