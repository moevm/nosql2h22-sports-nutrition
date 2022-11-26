import * as React from "react";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { NotFound } from "../NotFound";
import { getBranch } from "api/branch";
import { makeBranchDtoFromParams } from "../../api/functions";
import { HOST } from "../../constants";

export const FilteredBranchesList = () => {
  const params = useParams();
  console.log(params);
  const [branches, setBranches] = useState<any[]>([]);
  useEffect(() => {
    getBranch(makeBranchDtoFromParams(params))
      .then((response) => response.json())
      .then((json) => {
        setBranches(json.result);
      });
  }, [makeBranchDtoFromParams]);

  if (!branches.length) {
    return <NotFound />;
  }

  return (
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
      {branches.map((item) => {
        return (
          <tr key={item._id} className="branches-table">
            <td className="cell-id"
            ><a href={`${HOST}:8080/branch/id?_id=${item._id}`}>
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
  );

};