import { FilterProductCriteria } from "../../api/product";

export const updateField = (field: string, data: string, curValue: FilterProductCriteria,
                            setCurValue: (val: FilterProductCriteria) => void) => {
  const copy: FilterProductCriteria = { ...curValue };
  if (["_id", "descriptor_ids", "names",
    "price_from", "price_to", "supplier_ids"].indexOf(field) >= 0) {
    // @ts-ignore
    copy[field] = data.length ? data : undefined;
  }
  setCurValue(copy);
};