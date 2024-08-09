import { Map, MapMarker, CustomOverlayMap } from "react-kakao-maps-sdk";
import { useState } from 'react';

import data from '../../data.json';
import penisImage from '../../assets/penis.png'; 
import condomImage from '../../assets/condom.png'; 
import OverlayContent from "../OverlayComponent/OverlayContent.js";
import BottomPanel from "../BottomPanel/BottomPanel.js";



function KakaoMap() {
    const [activeMarker, setActiveMarker] = useState(null);
    const [selectedCategory, setSelectedCategory] = useState('sight');

    const handleCloseOverlay = () => {
        setActiveMarker(null);
    };

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setActiveMarker(null);
      };
    
      const filteredData = data.filter(item => item.ctgr === selectedCategory);


    return (
        <>
            <div id="mapwrap">
                <Map
                    id={`map`}
                    style={{ width: "100%", height: "100vh" }}
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
                                src:  selectedCategory === "sight" ? penisImage : condomImage,
                                size: {
                                  width: 24,
                                  height: 24,
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
