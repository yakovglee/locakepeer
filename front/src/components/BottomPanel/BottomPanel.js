import { Radio } from 'antd';
import './BottomPanel.css'

function BottomPanel () {

    return (
        <div className='bottomPanel'>

            <Radio.Group defaultValue={'sight'}>
                <Radio.Button value='sight'>Походить</Radio.Button>
                <Radio.Button value="caffe">Похавать</Radio.Button>
            </Radio.Group>
        
        </div>    
    )

}

export default BottomPanel;