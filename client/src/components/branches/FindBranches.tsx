import * as React from "react";
import {useEffect, useState} from "react";
import {FilterBranchCriteria, getFilteredBranches, isObjEmpty} from "api/branch";
import {checkObjOnNegativeNumbers, checkOnError, compareThenAlert} from "../../api/functions";
import {BranchesTable} from "./BranchesTable";
import {FindBranchDialog} from "./FindBranchDialog";
import {employeesRange, stocksRange} from "../../api/constants";


export const FindBranches = () => {
    const [branches, setBranches] = useState<any[]>([]);

    const [branchFilterCriteria, setBranchFilterCriteria] = useState<FilterBranchCriteria>({});


    useEffect(() => {
        if (isObjEmpty(branchFilterCriteria)) {
            return;
        }
        const checkOnNegative = checkObjOnNegativeNumbers(branchFilterCriteria);
        if (checkOnNegative.hasNegative) {
            alert(`${checkOnNegative.field} must be not negative`);
            return;
        }

        if (!compareThenAlert(stocksRange, branchFilterCriteria.stocks_from, branchFilterCriteria.stocks_to) ||
            !compareThenAlert(employeesRange, branchFilterCriteria.employees_from,
                branchFilterCriteria.employees_to))
            return;
        getFilteredBranches(branchFilterCriteria)
            .then((response) => checkOnError(response))
            .then((json) => {
                if (json) {
                    setBranches(json.result);
                }
            })
            .catch((err) => alert(err.message));
    }, [branchFilterCriteria, getFilteredBranches]);


    return (
        <>
            <FindBranchDialog onChange={setBranchFilterCriteria} value={branchFilterCriteria}/>
            {branches.length ? <BranchesTable branches={branches}/> : undefined}
        </>
    );

};