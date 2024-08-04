import { FacebookOutlined, InstagramOutlined, CloseOutlined } from '@ant-design/icons';
import { Card } from 'antd';
const { Meta } = Card;

const OverlayContent = ( {data, onClose} ) => (
  <Card type='inner' title={data.name} extra={<CloseOutlined onClick={onClose} />}
    style={{
        width: 300,
    }}
    actions={[
        <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer" key="link_inst">
            <InstagramOutlined  />
        </a>,

        <a href="https://www.fb.com" target="_blank" rel="noopener noreferrer" key="link_fb">
            <FacebookOutlined  />
        </a>,
    ]}
  >
    <Meta
      description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin id ultrices libero, et aliquam est. Vivamus bibendum faucibus enim, sit amet consequat est malesuada nec. Vivamus ut mi justo. Donec gravida facilisis massa, ut feugiat dolor vulputate volutpat. Cras tortor justo, tristique ut facilisis ac, dictum ac tortor. Sed dictum enim sed turpis eleifend fringilla. Nam ut auctor erat, eget luctus est. Suspendisse et diam convallis, pellentesque velit at, facilisis dolor. Mauris at ipsum maximus, posuere nisi at, rutrum odio. Nulla fermentum convallis accumsan. description"
    />
    <h3>Часы Работы { data.time }</h3>
    <h3>Доставка { data.pedal }</h3>
  </Card>
);

export default OverlayContent;