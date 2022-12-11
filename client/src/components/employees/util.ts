import { FilterEmployeesCriteria } from "../../api/branch";

export const updateField = (field: string, data: string, curValue: FilterEmployeesCriteria,
                            setCurValue: (val: FilterEmployeesCriteria) => void) => {
  const copy: FilterEmployeesCriteria = { ...curValue };

  if (["_id", "role", "phone_number", "name",
    "employment_date_from", "employment_date_to",
    "salary_from", "salary_to", "surname", "patronymic",
    "dismissal_date_from", "dismissal_date_to"].indexOf(field) >= 0) {
    // @ts-ignore
    copy[field] = data.length ? data : undefined;
  }
  setCurValue(copy);
};