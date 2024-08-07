import Icon, { InstagramOutlined, CloseOutlined } from '@ant-design/icons';
import { Card } from 'antd';
import './OverlayContentStyle.css';
const { Meta } = Card;


const NaverSvg = () => (
    <svg width="15" height="15" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g clip-path="url(#clip0_403_243)">
    <path d="M18 20H2C0.9 20 0 19.1 0 18V2C0 0.9 0.9 0 2 0H18C19.1 0 20 0.9 20 2V18C20 19.1 19.1 20 18 20Z" fill="#03C75A"/>
    <path d="M11.35 10.25L8.50002 6.19995H6.15002V13.8H8.65002V9.74995L11.5 13.8H13.85V6.19995H11.35V10.25Z" fill="white"/>
    </g>
    <defs>
    <clipPath id="clip0_403_243">
    <rect width="20" height="20" fill="white"/>
    </clipPath>
    </defs>
    </svg>
);

const NaverIcon = (props) => <Icon component={NaverSvg} {...props} />;

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

    <a className="link_kakao" href={`https://map.kakao.com/link/map/${data.name_en},${data.position.lat},${data.position.lng}`} target="_blank">На карте</a>
    
  </Card>
);

export default OverlayContent;