import * as React from "react";
import { useEffect, useState } from "react";
import "./Branches.scss";
import { Pagination } from "../pagination/Pagination";

const pageSize = 15;

export const BranchesList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);
  const [lastPage, setLastPage] = useState(false);

  useEffect(() => {
    console.log("Current page: ", currentPage);
    fetch(`http://localhost:8008/branch/page?size=${pageSize}&page=${currentPage}`, {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" }
    })
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
          <th>Branch Id</th>
          <th>Name</th>
          <th>Employees</th>
          <th>Location</th>
        </tr>
        </thead>
        <tbody>
        {data.map((item) => {
          return (
            <tr key={item._id} className="branches-table">
              <td className="cell-id">{item._id}</td>
              <td>{item.name}</td>
              <td>0</td>
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
    </>
  );
};
