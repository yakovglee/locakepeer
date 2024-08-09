import React from 'react';
import { Radio } from 'antd';
import './BottomPanel.css';

const BottomPanel = ({ selectedCategory, onCategoryChange }) => {

  return (
    <div className='bottomPanel'>
      <Radio.Group 
        value={selectedCategory} 
        onChange={onCategoryChange}
      >
        <Radio.Button value='sight'>Походить</Radio.Button>
        <Radio.Button value='caffe'>Похавать</Radio.Button>
      </Radio.Group>
    </div>
  );
};

export default BottomPanel;
