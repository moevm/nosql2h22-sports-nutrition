import React from "react";
import classnames from "classnames";
import { List, ListItem, ListItemButton, ListItemIcon } from "@mui/material";
import KeyboardArrowLeftIcon from "@mui/icons-material/KeyboardArrowLeft";
import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";

interface PaginationProps {
  onPageChange: (page: number) => void;
  currentPage: number;
  lastPage: boolean;
  className: string;
}

export const Pagination = (props: PaginationProps) => {

  const {
    onPageChange,
    currentPage,
    className,
    lastPage
  } = props;

  const onNext = () => {
    onPageChange(currentPage + 1);
  };

  const onPrevious = () => {
    onPageChange(currentPage - 1);
  };

  return (
    <List style={{ display: "flex", alignSelf: "center", justifyContent: "center" }}
          className={classnames("pagination-container", { [className]: className })}>
      <ListItem
        style={{ width: "10%" }}
        key={currentPage + className}
      >
        <ListItemButton onClick={onPrevious}
                        disabled={currentPage <= 1}> <ListItemIcon>
          <KeyboardArrowLeftIcon />
        </ListItemIcon> </ListItemButton>
      </ListItem>

      <ListItem
        style={{ width: "5%" }}
        key={currentPage}
      >
        {currentPage}
      </ListItem>

      <ListItem
        style={{ width: "10%" }}
        key={"pagination-item-disabled"}
      >
        <ListItemButton disabled={lastPage} onClick={() => {
          onNext();
        }}> <ListItemIcon>
          <KeyboardArrowRightIcon />
        </ListItemIcon> </ListItemButton>
      </ListItem>
    </List>
  );
};
