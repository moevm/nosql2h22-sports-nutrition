import * as React from "react";
import {useEffect, useState} from "react";
import DialogContent from "@mui/material/DialogContent";
import {Box, TextField, Typography} from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import "../dialog.scss";
import {FilterBranchCriteria, isObjEmpty} from "api/branch";
import {updateField} from "./util";

interface FindBranchProps {
    onChange: (val: FilterBranchCriteria) => void,
    value: FilterBranchCriteria
}

export function FindBranchDialog(props: FindBranchProps) {
    const {value, onChange} = props;
    const [curVal, setCurVal] = useState<FilterBranchCriteria>({});

    useEffect(() => {
        setCurVal(value);
    }, [value]);


    return (
        <Box width="70%">
            <Typography variant="h5">
                Find branches
            </Typography>
            <DialogContent dividers>
                <TextField
                    margin="dense"
                    id="id"
                    label="Id"
                    fullWidth
                    onChange={(val) =>
                        updateField("_id", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />
                <TextField
                    margin="dense"
                    id="name"
                    label="Name"
                    fullWidth
                    onChange={(val) =>
                        updateField("name", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />
                <TextField
                    margin="dense"
                    id="city"
                    label="City"
                    fullWidth
                    onChange={(val) =>
                        updateField("city", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />

                <TextField
                    margin="dense"
                    type="number"
                    id="stocks_from"
                    label="Stocks from"
                    fullWidth
                    onChange={(val) =>
                        updateField("stocks_from", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />

                <TextField
                    margin="dense"
                    id="stocks_to"
                    type="number"
                    label="Stocks to"
                    fullWidth
                    onChange={(val) =>
                        updateField("stocks_to", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />

                <TextField
                    margin="dense"
                    type="number"
                    id="employees_from"
                    label="Employee from"
                    fullWidth
                    onChange={(val) =>
                        updateField("employees_from", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />

                <TextField
                    margin="dense"
                    type="number"
                    id="employees_to"
                    label="Employee to"
                    fullWidth
                    onChange={(val) =>
                        updateField("employees_to", val.target.value, curVal, setCurVal)}
                    variant="standard"
                />

                <TextField
                    margin="dense"
                    id="employee_ids"
                    label="Employee ids"
                    fullWidth
                    placeholder="id1, id2"
                    onChange={(val) =>
                        updateField("employee_ids", val.target.value, curVal, setCurVal)}
                    variant="standard"
                    helperText={`Use "," between ids of employees. Example: "id1, id2"`}
                />
                <TextField
                    margin="dense"
                    id="employee_names"
                    label="Employee names"
                    fullWidth
                    placeholder="name1, name2"
                    onChange={(val) =>
                        updateField("employee_names", val.target.value, curVal, setCurVal)}
                    variant="standard"
                    helperText={`Use "," between names of employees. Example: "name1, name2"`}
                />
                <TextField
                    margin="dense"
                    id="employee_surnames"
                    label="Employee surnames"
                    fullWidth
                    placeholder="surname1, surname2"
                    onChange={(val) =>
                        updateField("employee_surnames", val.target.value, curVal, setCurVal)}
                    variant="standard"
                    helperText={`Use "," between surnames of employees. Example: "surname1, surname2"`}
                />
                <TextField
                    margin="dense"
                    id="product_ids"
                    label="Product ids"
                    fullWidth
                    placeholder="id1, id2"
                    onChange={(val) =>
                        updateField("product_ids", val.target.value, curVal, setCurVal)}
                    variant="standard"
                    helperText={`Use "," between ids of products. Example: "id1, id2"`}
                />
                <TextField
                    margin="dense"
                    id="supplier_ids"
                    label="Product names"
                    fullWidth
                    placeholder="name1, name2"
                    onChange={(val) =>
                        updateField("product_names", val.target.value, curVal, setCurVal)}
                    variant="standard"
                    helperText={`Use "," between names of products. Example: "name1, name2"`}
                />

            </DialogContent>
            <DialogActions>
                <Button autoFocus onClick={() => onChange(curVal)}
                        disabled={isObjEmpty(curVal)}>
                    Find
                </Button>
            </DialogActions>
        </Box>
    );
}
