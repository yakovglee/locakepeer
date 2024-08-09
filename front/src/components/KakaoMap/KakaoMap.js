import { Map, MapMarker, CustomOverlayMap } from "react-kakao-maps-sdk";
import { useState } from 'react';

import data from '../../data.json';
import './KakaoMap.css'; 
import OverlayContent from "../OverlayComponent/OverlayContent.js";
import BottomPanel from "../BottomPanel/BottomPanel.js";

function KakaoMap() {
    const [activeMarker, setActiveMarker] = useState(null);
    const [selectedCategory, setSelectedCategory] = useState('sight');


    const handleCategoryChange = (e) => {
      console.log(e.target.value)
      setSelectedCategory(e.target.value);
    };
  
    const filteredData = data.filter(item => item.ctgr === selectedCategory);

    const handleCloseOverlay = () => {
        setActiveMarker(null);
    };

    return (
        <>
            <div id="mapwrap">
                <Map
                    id={`map`}
                    center={{
                        lat: 36.2683,
                        lng: 127.6358,
                    }}
                    level={13}
                >
                    {filteredData.map((obj) => (
                        <MapMarker
                            key={obj.id} 
                            position={obj.position}
                            image={{
                                src: "./markerSign.png", 
                                size: {
                                    width: 24,
                                    height: 30
                                }, 
                            }}
                            onClick={() => setActiveMarker(obj)} 
                        />
                    ))}
                    
                    {activeMarker && (
                        <CustomOverlayMap position={activeMarker.position}>
                            <OverlayContent
                                data={activeMarker}
                                onClose={handleCloseOverlay} 
                            />
                        </CustomOverlayMap>
                    )}

                    


                    <BottomPanel 
                        selectedCategory={selectedCategory}
                        onCategoryChange={handleCategoryChange}
                    />
                </Map>
            </div>
        </>
    );
}

export default KakaoMap;
