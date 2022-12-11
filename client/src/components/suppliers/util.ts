import {FilterSupplierCriteria} from "../../api/supplier";


export const updateField = (field: string, data: string, curValue: FilterSupplierCriteria,
                            setCurValue: (val: FilterSupplierCriteria) => void) => {
  const copy: FilterSupplierCriteria = { ...curValue };

  if (["_id", "email", "phone", "name",
    "product_ids", "descriptor_ids",
    "product_names"].indexOf(field) >= 0) {
    // @ts-ignore
    copy[field] = data.length ? data : undefined;
  }
  setCurValue(copy);
};