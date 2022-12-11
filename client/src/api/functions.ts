import {Params} from "react-router-dom";

export function toQueryString(obj: any) {
    const keyValuePairs = [];
    for (const key in obj) {
        if (obj[key] && obj[key] !== " ") {
            keyValuePairs.push(encodeURIComponent(key) + "=" + encodeURIComponent(obj[key]));
        }
    }
    return keyValuePairs.join("&");
}


export async function checkOnError(response: Response, okMessage?: string) {
    if (response.ok) {
        if (okMessage)
            alert(okMessage);
        return response.json();
    } else {
        const res = await response.text();
        alert(JSON.parse(res).message);
        return undefined;
    }
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
    if (!date.length) {
        return "";
    }
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

function isNumeric(str: any) {
    return !isNaN(str) && !isNaN(parseFloat(str))
}

export const checkObjOnNegativeNumbers = (obj: any): { hasNegative: boolean, field?: string } => {
    for (const [key, value] of Object.entries(obj)) {
        if (value && isNumeric(value) && Number(value) < 0) {
            return {hasNegative: true, field: key};
        }
    }
    return {hasNegative: false};
};


export const compareThenAlert = (message: string, from?: string, to?: string) => {
    if (Number(from) > Number(to)) {
        alert(message);
        return false;
    }
    return true;
}