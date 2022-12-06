import { Params } from "react-router-dom";

export function toQueryString(obj: any) {
  const keyValuePairs = [];
  console.log("OBJ: ", obj);
  for (const key in obj) {
    console.log("key: ", key, obj[key]);
    if (obj[key] && obj[key] !== " ") {
      keyValuePairs.push(encodeURIComponent(key) + "=" + encodeURIComponent(obj[key]));
    }
  }
  return keyValuePairs.join("&");
}

export interface GetBranchDto {
  name?: string;
  _id?: string;
  city?: string;
}

export const branchDtoFromParams = (params: Readonly<Params<string>>): GetBranchDto => {
  return {
    name: params.name,
    city: params.city,
    _id: params._id
  };
};

export const branchDtoFromStrings = (name: string, city: string, id: string): GetBranchDto => {
  return {
    name: name.length ? name : undefined,
    city: city.length ? city : undefined,
    _id: id.length ? id : undefined
  };
};

export const toServerDateFormat = (date: string) => {
  //"1/1/2020 1:1:1",
  // 2022-12-11T12:43
  const monthSeparatorIndex = date.indexOf("-");
  const daySeparatorIndex = date.lastIndexOf("-");
  const hoursSeparator = date.indexOf("T");
  const minutesSeparator = date.indexOf(":");
  let year = date.slice(0, monthSeparatorIndex);
  const month = date.slice(monthSeparatorIndex + 1, daySeparatorIndex);
  const day = date.slice(daySeparatorIndex + 1, hoursSeparator);
  const hours = date.slice(hoursSeparator + 1, minutesSeparator);
  const minutes = date.slice(minutesSeparator + 1);
  const currentYear = new Date().getFullYear();
  if (Number(year) > currentYear) {
    year = String(currentYear);
  }

  return day + "/" + month + "/" + year + " " + hours + ":" + minutes + ":0";
};

export const checkObjOnDefault = (obj: any) => {
  if (!obj) {
    return true;
  }
  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === "string" && value.length === 0 ||
      typeof value === "number" && value < 0) {
      return true;
    }
  }
  return false;
};

export const checkObjOnNegativeNumbers = (obj: any) => {
  for (const [key, value] of Object.entries(obj)) {
    if (value && typeof value === "number" && value < 0) {
      return true;
    }
  }
  return false;
};