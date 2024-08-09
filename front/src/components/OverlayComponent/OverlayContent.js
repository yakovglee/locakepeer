import { InstagramOutlined, CloseOutlined } from '@ant-design/icons';
import { Card } from 'antd';

import NaverIcon from './NaverIcon'
import './OverlayContentStyle.css';

const { Meta } = Card;

const OverlayContent = ( {data, onClose} ) => (

  <Card type='inner' title={data.name_ko} extra={<CloseOutlined onClick={onClose} />}
    style={{width: 300,}}
    className="custom-card"
    actions={[
        <a href={data.insta} target="_blank" rel="noopener noreferrer" key="link_inst">
            <InstagramOutlined  />
        </a>,
        <a href={data.namuWiki} target="_blank" rel="noopener noreferrer" key="link_inst">
        <NaverIcon  />
    </a>,
    ]}
  >
    {data.name_en}
    
    <div className="card-content">
      <Meta description={data.description} />
    </div>

    <a className="link_kakao" href={`https://map.kakao.com/link/map/${data.name_en},${data.position.lat},${data.position.lng}`} target="_blank" rel="noopener">На карте</a>
    
  </Card>
);

export default OverlayContent;