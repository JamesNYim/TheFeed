import { api } from "./client";

async function getPosts({ limit = 10, feed_cursor = null} = {}) {
    const params = new URLSearchParams();
    params.set("limit", limit);
    if (feed_cursor) {
        params.set("feed_cursor", String(feed_cursor));
    }

    return api(`/posts?${params.toString()}`, { method: "GET" });

}
export default getPosts;
