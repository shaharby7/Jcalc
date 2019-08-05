import axios from 'axios'
import { pathToFileURL } from 'url';
import path from 'path';

// TODO: Move configuration to backend

backendConfig = {
    "base_url": "http://localhost:8081/juggling",
    "routes": {
        "debugger": "debugger"
    }
}

getBackendUrl = (requiredSerice) => {
    return path.join(backendConfig.base_url, backendConfig.routes[requiredSerice]);
}

debggerService = async (siteswap) => {
    const url = getBackendUrl("debugger");
    const response = await axios.post(url = url, json = { "siteswap": siteswap })
    return response
}