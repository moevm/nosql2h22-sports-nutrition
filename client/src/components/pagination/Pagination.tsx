import React from 'react';
import classnames from 'classnames';
import './pagination.scss';

export const Pagination = ({
  onPageChange,
  currentPage,
  className,
  lastPage
}: {
  onPageChange: (page: number) => void;
  currentPage: number;
  lastPage: boolean;
  className: string;
}) => {

  const onNext = () => {
    onPageChange(currentPage + 1);
  };

  const onPrevious = () => {
    onPageChange(currentPage - 1);
  };

  return (
    <ul className={classnames('pagination-container', { [className]: className })}>
      <li
        key={currentPage+className}
        className={classnames('pagination-item', {
          disabled: currentPage === 1,
        })}
        onClick={onPrevious}
      >
        <div className="arrow left" />
      </li>
      <li
        key={currentPage}
        className={classnames('pagination-item')}
        >
        {currentPage}
        </li>

      <li
        key={'pagination-item-disabled'}
        className={classnames('pagination-item', {
          disabled: lastPage
        })}
        onClick={() => {
          console.log("LastPage :", lastPage);
          onNext()}}
      >
        <div className="arrow right" />
      </li>
    </ul>
  );
};
