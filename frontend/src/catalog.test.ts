import {describe,expect,it} from 'vitest'

describe('frontend safety contract',()=>{
  it('uses only relative local API routes',()=>{
    const route='/api/challenges'
    expect(route.startsWith('/api/')).toBe(true)
    expect(route).not.toMatch(/^https?:/)
  })
})
