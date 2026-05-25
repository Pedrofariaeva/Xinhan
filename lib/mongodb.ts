import { MongoClient } from 'mongodb'

const uri = process.env.MONGODB_URI

let clientPromise: Promise<MongoClient> | undefined

function getClientPromise(): Promise<MongoClient> {
  if (!uri) {
    throw new Error('MONGODB_URI environment variable is not set')
  }
  if (clientPromise) return clientPromise

  if (process.env.NODE_ENV === 'development') {
    const globalWithMongo = global as typeof globalThis & {
      _mongoClientPromise?: Promise<MongoClient>
    }
    if (!globalWithMongo._mongoClientPromise) {
      const client = new MongoClient(uri)
      globalWithMongo._mongoClientPromise = client.connect()
    }
    clientPromise = globalWithMongo._mongoClientPromise
  } else {
    const client = new MongoClient(uri)
    clientPromise = client.connect()
  }
  return clientPromise
}

export async function getDb(name: string = process.env.DB_NAME ?? 'xinhan') {
  const client = await getClientPromise()
  return client.db(name)
}
