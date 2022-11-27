import * as React from "react";
import { useEffect, useState } from "react";
import "./Branches.scss";
import { Pagination } from "../pagination/Pagination";
import { HOST } from "../../constants";
import { getBranchesPage } from "../../api/branch";

const pageSize = 15;

export const BranchesList = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [data, setData] = useState<any[]>([]);
  const [lastPage, setLastPage] = useState(false);

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
              <td className="cell-id"
              ><a href={`${HOST}8080/branch/id/${item._id}`}>
                {item._id}
              </a></td>
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
