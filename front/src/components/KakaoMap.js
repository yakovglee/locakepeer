import { Map, MapMarker, CustomOverlayMap } from "react-kakao-maps-sdk";
import { useState } from 'react';

import data from '../data.js';
import OverlayContent from "./OverlayContent.js";

function KakaoMap() {
    const [activeMarker, setActiveMarker] = useState(null);

    const handleCloseOverlay = () => {
        setActiveMarker(null);
    };

    return (
        <>
            <div id="mapwrap">
                <Map
                    id={`map`}
                    center={{
                        lat: 37.5665,
                        lng: 126.978,
                    }}
                    style={{
                        width: "100%",
                        height: "450px",
                    }}
                    level={10}
                >
                    {data.map((obj) => (
                        <MapMarker
                            key={obj.id} 
                            position={obj.position}
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
                </Map>
            </div>
        </>
    );
}

export default KakaoMap;
