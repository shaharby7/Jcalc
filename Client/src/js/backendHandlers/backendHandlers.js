import axios from 'axios'
import { pathToFileURL } from 'url';
import path from 'path';

// TODO: Move configuration to backend

const backendConfig = {
    "protocol": "http",
    "hostname": "localhost",
    "port": 8081,
    "routes": {
        "analyzer": "juggling/analyzer"
    }
}

axios.defaults.port = backendConfig.port;

const baseBackendUrl = backendConfig.protocol
    + '://' + backendConfig.hostname
    + ':' + backendConfig.port;

const getFullUrlPath = (requiredPath) => {
    return baseBackendUrl + "/" + backendConfig.routes[requiredPath];
}

export const analyzeService = async (siteswap) => {
    const path = getFullUrlPath("analyzer");
    const response = await axios.post(path, { "siteswap": siteswap });
    const data = await response.data;
    data.beatmap = JSON.parse(data.beatmap);
    data.problems = JSON.parse(data.problems);
    return response.data;
}