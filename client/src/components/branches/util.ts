import {FilterBranchCriteria} from "../../api/branch";

export const updateField = (field: string, data: string, curValue: FilterBranchCriteria,
                            setCurValue: (val: FilterBranchCriteria) => void) => {
  const copy: FilterBranchCriteria = { ...curValue };

  if (["_id", "name", "city", "product_names", "stocks_to",
    "stocks_from", "employee_names", "employees_from", "employees_to",
    "employee_surnames", "employee_ids", "product_ids"].indexOf(field) >= 0) {
    // @ts-ignore
    copy[field] = data.length ? data : undefined;
  }
  setCurValue(copy);
};